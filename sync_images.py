import os
import re
import shutil

# Paths
posts_dir = "/home/sluggishthingg/Documents/sluggishthinggblog/content/posts/"
attachments_dir = "/home/sluggishthingg/Documents/Obsidian Vault/Attachments/"
static_images_dir = "/home/sluggishthingg/Documents/sluggishthinggblog/static/images/"

# Process markdown files
for filename in os.listdir(posts_dir):

    if filename.endswith(".md"):

        filepath = os.path.join(posts_dir, filename)

        with open(filepath, "r") as file:
            content = file.read()

        # Find Obsidian image embeds
        images = re.findall(r'!\[\[([^]]*\.png)\]\]', content)

        for image in images:

            # Replace Obsidian syntax with Hugo markdown syntax
            markdown_image = f"![Image](/images/{image.replace(' ', '%20')})"

            content = content.replace(f"![[{image}]]", markdown_image)

            # Copy image to Hugo static/images
            image_source = os.path.join(attachments_dir, image)

            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Save updated markdown
        with open(filepath, "w") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")
