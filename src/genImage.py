from diffusers import StableDiffusionPipeline
import torch
import os

def generate(prompt: str, w: int = 512, h: int = 512):
    torch.mps.empty_cache()

    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32,
        use_safetensors=True
    )
    pipe.to("mps")
    pipe.enable_attention_slicing()

    image = pipe(prompt, height=512, width=512).images[0]

    output_dir = "assets/generated"
    os.makedirs(output_dir, exist_ok=True) 
    image_path = os.path.join(output_dir, f"{"_".join(prompt.split())}.png")
    image.save(image_path)

    print(f"✅ Image saved to {image_path}")

if __name__ == "__main__":
    generate("naruto uzumaki")
