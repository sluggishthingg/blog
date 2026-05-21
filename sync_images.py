import os
import re
import shutil

# Paths
posts_dir = "/home/sluggishthingg/Documents/sluggishthinggblog/content/posts/"
attachments_dir = "/home/sluggishthingg/Documents/Obsidian Vault/Attachments/"
static_images_dir = "/home/sluggishthingg/Documents/sluggishthinggblog/static/images/"

# Create static/images if it doesn't exist
os.makedirs(static_images_dir, exist_ok=True)

# Process markdown files
for filename in os.listdir(posts_dir):

    if filename.endswith(".md"):

        filepath = os.path.join(posts_dir, filename)

        # Read markdown content
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        # Find markdown image links
        images = re.findall(r'!\[\]\((.*?)\)', content)

        for image in images:

            # Convert %20 back to spaces for filesystem lookup
            image_name = image.replace('%20', ' ')

            print(f"Processing image: {image_name}")

            # Create correct Hugo image path
            markdown_image = f"![](/images/{image})"

            # Replace old markdown path
            content = content.replace(
                f"![]({image})",
                markdown_image
            )

            # Source image path
            image_source = os.path.join(
                attachments_dir,
                image_name
            )

            # Copy image if exists
            if os.path.exists(image_source):

                shutil.copy(
                    image_source,
                    static_images_dir
                )

                print(f"Copied: {image_name}")

            else:
                print(f"Image not found: {image_name}")

        # Save updated markdown
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed successfully.")
