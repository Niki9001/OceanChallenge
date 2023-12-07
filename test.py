from pathlib import Path
from openai import OpenAI
import openai
key = "  "
client = OpenAI(api_key=key)

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="Shimmer",
  input="""PAGE 1 
Today, I am thrilled to introduce to you the gateway to a magnificent marine adventure - the Home Page of the Gulf of St. Lawrence website. This platform is not just a website; it's a virtual odyssey, a bridge between our daily lives and the vast, mysterious world of the ocean.

Our journey begins with the 'Oceanic Odyssey'. This section is a deep dive into the heart of marine data, offering users an unparalleled view of the ocean's health and dynamics. Leveraging the latest scientific data, we bring to life the ever-changing tapestry of marine life and environmental conditions. It's here that the ocean's story is told, not in numbers, but through interactive visualizations and engaging narratives.


Next, we navigate to the 'Encyclopedia'. This treasure trove of marine biology is where curiosity meets knowledge. Delving into this section, users of all ages can explore the rich biodiversity of the Gulf. It's a comprehensive guide, filled with fascinating facts about marine species, their habitats, and the roles they play in the ocean's ecosystem. It's not just an encyclopedia; it's a portal to understanding and appreciating the life beneath the waves.


The 'Leisure' section is our tribute to the joy and serenity that the ocean brings to our lives. Here, we've curated a guide to help users find the perfect marine leisure spots. Whether it's finding the best locations to witness the majestic whale migrations or discovering serene beaches for a family outing, this section is about making those magical ocean moments happen.

Finally, we have 'Sea Sketch', a special place designed for our youngest ocean explorers. In this interactive and creative space, children can engage with the ocean in a unique way. They can create and visualize their own ocean adventures, bringing them closer to marine life and fostering an early love for the marine world.

PAGE 2
The 'Oceanic Odyssey' section of our website stands as a testament to our commitment to bringing the most current and comprehensive understanding of the marine environment to our users. The heart of this endeavor is our partnership with CIOOS, from whom we source our data. Through sophisticated coding, we have established an automated system that downloads updates from CIOOS as soon as they become available. This ensures that our page is always reflecting the most up-to-date information, offering users a vivid and accurate portrayal of the marine ecosystem in the Gulf of St. Lawrence.

In 'Oceanic Odyssey', we don't just present data; we bring it to life. Our platform highlights intriguing discoveries and trends in the marine world. For instance, we encourage users to engage with and reflect on the increasing biodiversity in the region. Is the rising diversity index truly a positive sign? We prompt such thoughtful inquiries. Additionally, we bring attention to significant ecological shifts, such as the increasing presence of the dusky, a species traditionally found in the northern parts of Australia. As surface temperatures rise, they are now more frequently observed in our waters. This migration, intriguing in its own right, also prompts consideration of its impact on the indigenous marine species of the Gulf.

Through 'Oceanic Odyssey', we aim to not just inform, but to inspire a deeper understanding and contemplation about the delicate balance and dynamic changes in our ocean's ecosystem.

PAGE 3

In the 'Leisure' section of our website, we have crafted a unique navigation tool designed to enhance the recreational experiences of our users. At the core of this feature is a sophisticated machine learning model, developed using extensive data collected from 1970 to 2019. This model enables us to predict the likelihood of encountering various marine species at specific latitudes and longitudes with remarkable precision. Users can interact with this tool in two ways: they can enter their coordinates of interest to receive tailored information, or they can simply click on our intuitive icons for instant insights.

But our commitment to enhancing your leisure experience doesn't stop there. We understand that a fulfilling ocean outing involves more than just spotting marine life; it's also about understanding the environment you're stepping into. Therefore, we provide detailed information on the nearshore conditions of different marine areas. This includes data on water quality, temperature, and other relevant environmental factors, ensuring that our users can easily access all the information they need to plan their perfect ocean getaway. Whether you're a seasoned marine enthusiast or a casual beachgoer, our 'Leisure' page is designed to make your next ocean adventure both informed and memorable.

PAGE 4
The 'Encyclopedia' section of our website is a dynamic and engaging portal, specifically crafted to captivate the curiosity of young minds towards the marine world. This comprehensive marine encyclopedia is the result of an innovative fusion of our extensive database, which documents the myriad of marine species found in our region, and the detailed data from the FishBase API. By comparing and combining these rich sources of information, we provide a thorough and fascinating view of oceanic life.

But the true magic happens when we integrate AI technology into this mix. The AI API works to tailor the content in a way that is particularly appealing to teenagers, making the complexities of marine biology both accessible and engaging. This interactive platform not only delivers facts but also encourages exploration and learning through intuitive interfaces and captivating visuals.

In this space, young users are invited to delve deep into their oceanic curiosities. They can learn about the diverse species that inhabit our waters, their behaviors, habitats, and the ecological roles they play. This section is more than just an educational resource; it's a launchpad for the next generation of marine enthusiasts, conservationists, and scientists, sparking a lifelong passion and respect for the ocean's wonders.

PAGE 5

The 'Sea Sketch' section of our website is a delightful and interactive space designed for children of all ages, aimed at fostering a deep and enduring love for the ocean. In this unique digital environment, children have the opportunity to blend their world with that of marine life in an imaginative and engaging way. By uploading their photos, they can utilize our specially fine-tuned OpenAI model to create enchanting images that depict them alongside various sea creatures. This innovative feature not only brings a sense of wonder and excitement but also helps in building a personal connection between the young users and the marine world.

Our goal with 'Sea Sketch' is to provide a platform that not only entertains but also educates and inspires. By allowing children to visualize themselves in the company of marine life, we open up a world of possibilities for them to explore and learn about the ocean. This immersive experience is more than just a fun activity; it serves as a gentle nudge towards a lifelong journey of discovery and appreciation of the ocean's wonders.

We believe that by giving children this opportunity to explore and connect with the ocean, we are paving the way for a brighter future. A future where the next generation is more informed, more connected, and more committed to the stewardship of our oceans than ever before. 'Sea Sketch' is more than just a page on a website; it's a portal to possibilities and a seed for future growth and better care of our marine environment.


"""
)
response.stream_to_file(speech_file_path)

