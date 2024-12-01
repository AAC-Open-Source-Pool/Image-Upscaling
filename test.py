import os
import torch
from torchvision.transforms import functional as F
from PIL import Image
import torch.nn as nn

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class ResidualBlock(nn.Module):
    def __init__(self, num_features):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(num_features, num_features, kernel_size=3, padding=1)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(num_features, num_features, kernel_size=3, padding=1)

    def forward(self, x):
        residual = x
        out = self.conv1(x)
        out = self.relu(out)
        out = self.conv2(out)
        out = out * 0.1  
        return out + residual

class EDSR(nn.Module):
    def __init__(self, num_blocks=32, num_features=256, scale_factor=4):
        super(EDSR, self).__init__()
        self.input_conv = nn.Conv2d(3, num_features, kernel_size=3, padding=1)
        self.residual_blocks = nn.Sequential(
            *[ResidualBlock(num_features) for _ in range(num_blocks)]
        )
        self.output_conv = nn.Conv2d(num_features, num_features, kernel_size=3, padding=1)
        self.upsample = nn.Conv2d(num_features, 3 * (scale_factor ** 2), kernel_size=3, padding=1)
        self.pixel_shuffle = nn.PixelShuffle(scale_factor)

    def forward(self, x):
        x = self.input_conv(x)
        residual = x
        x = self.residual_blocks(x)
        x = self.output_conv(x)
        x += residual
        x = self.upsample(x)
        x = self.pixel_shuffle(x)
        return x

def load_model(model_path, scale_factor=4):
    model = EDSR(scale_factor=scale_factor).to(DEVICE)
    state_dict = torch.load(model_path, map_location=DEVICE)

    # If used multiple GPU during training
    if any(key.startswith("module.") for key in state_dict.keys()):
        state_dict = {key.replace("module.", ""): value for key, value in state_dict.items()}

    model.load_state_dict(state_dict)
    model.eval()
    return model

def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')
    image_tensor = F.to_tensor(image).unsqueeze(0).to(DEVICE)
    return image, image_tensor

def postprocess_image(output_tensor):
    output_tensor = output_tensor.squeeze(0).cpu()
    output_tensor = torch.clamp(output_tensor, 0, 1)
    output_image = F.to_pil_image(output_tensor)
    return output_image

def upscale_image(image_path, output_path, model):
    original_image, image_tensor = preprocess_image(image_path)
    with torch.no_grad():
        upscaled_tensor = model(image_tensor)

    upscaled_image = postprocess_image(upscaled_tensor)
    upscaled_image.save(output_path)
    print(f"Upscaled image saved to: {output_path}")

def upscale_directory(input_dir, output_dir, model):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in sorted(os.listdir(input_dir)):
        input_path = os.path.join(input_dir, filename)
        if os.path.isfile(input_path) and filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'tiff')):
            output_path = os.path.join(output_dir, filename)
            upscale_image(input_path, output_path, model)


if __name__ == "__main__":
    model_path = "Models\\edsr_best_x4.pth"  
    input_dir = "Input"  
    output_dir = "Upscaled"
    scale_factor = 4
    model = load_model(model_path, scale_factor)
    upscale_directory(input_dir, output_dir, model)
