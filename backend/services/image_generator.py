import os
def generate_image(prompt: str):

    try:
        os.makedirs("storage/generated", exist_ok=True)

        filename = f"{uuid.uuid4().hex}.png"
        path = f"storage/generated/{filename}"

        image_prompt = f"Professional 1080x1080 social media poster for: {prompt}"

        response = client.models.generate_images(
            model="imagen-3.0-generate-002",
            prompt=image_prompt
        )

        generated_image = response.generated_images[0].image
        generated_image.save(path)

        return f"/storage/generated/{filename}"

    except Exception as e:
        print("Image generation failed, using fallback:", e)

        from PIL import Image, ImageDraw

        img = Image.new("RGB", (1080, 1080), color=(15, 23, 42))
        draw = ImageDraw.Draw(img)

        draw.text((100, 100), "AI SOCIAL POST", fill="white")
        draw.text((100, 250), prompt[:100], fill="white")

        fallback_path = "storage/generated/fallback.png"
        img.save(fallback_path)

        return "/storage/generated/fallback.png"