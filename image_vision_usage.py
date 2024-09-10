from load_client import load_client
from config import Config
client = load_client()
# this function allows text models to understand images, as a separate function call with listening for image urls in user responses in chat later.
def generate_image_vision_text(image_url):
    response = client.chat.completions.create(
        model=Config.image_vision_model,
        messages=[
            {"role": "user", "content": f"Generate a text description of the image at {image_url}"}
        ],
        response_format={"type": "text"}
    )
    return response.choices[0].message.content
# # test the function
# image_url = "https://i.imgur.com/ygrwfdW.jpeg"
# print(generate_image_vision_text(image_url))
# output below:

# Title: A Dreamer's Paradise? - A Mixed Reality Vacation Resort
# Width: 1440
# Height: 960
# Framerate: 60

# The image presents a panoramic view of a relaxing beach getaway that combines the natural environment with advanced, futuristic technology. The scene captures a resort area with an exotic aesthetic design, featuring various buildings, beach elements, and otherworldly architectural elements. The vacation resort is thoughtfully situated near a large body of water, offering picturesque views for visitors to enjoy.

# Numerous people can be seen at the resort, either standing, walking, or relaxing within the scene. Some are closer to the foreground, while others are positioned further back, giving off an impression of an active, vibrant destination. There is a series of umbrellas dotted around the beach, providing shade and shelter from the sun.

# In the middle of the resort, a luxury liner boat gently sways on the wide body of water, adding to the dreamlike atmosphere of the scene. The boat takes center stage, drawing attention to the beachgoers and creating a fascinating contrast between the natural environment and the technological marvels that have come to enhance their leisure experience.
