# faq-bot
Server to perform NLU and NLP on incoming WhatsApp messages

## Tools & Technologies used
- Python 3.8.13
- Rasa

## Steps to run locally
1. Clone this repo
    ```sh
    git clone https://github.com/hanzala-sohrab/faq-bot.git
    ```
2. Change directory
    ```sh
    cd faq-bot
    ```
3. Create a virtual environment and activate it
    ```sh
    python3.8 -m venv venv && source venv/bin/activate
    ```
4. Install required libraries
    ```sh
    pip3.8 install -r requirements.txt
    ```
5. Train the model (this step is required if any change is made to any of the `yml` files)
    ```sh
    rasa train
    ```
6. Start the server
    ```sh
    rasa run
    ```

## Demo
- **Getting college info like name, address, branches, placement stats, etc.**

https://user-images.githubusercontent.com/40603380/165647415-a4e98da9-fd54-4c32-b8b9-f953646111ab.mp4

- **Getting faculty information**

https://user-images.githubusercontent.com/40603380/165648106-a05ae0cb-7499-4401-b1b8-e767cdc7d45a.mp4


## Rasa architecture

![image](https://user-images.githubusercontent.com/40603380/165640494-783b690b-cc9e-4e8e-b6ce-d303e0e31410.png)

- The diagram above provides an overview of the Rasa Open Source architecture. The two primary components are Natural Language Understanding (NLU) and dialogue management.

- NLU is the part that handles intent classification, entity extraction, and response retrieval. It's shown below as the NLU Pipeline because it processes user utterances using an NLU model that is generated by the trained pipeline.

- The dialogue management component decides the next action in a conversation based on the context. This is displayed as the Dialogue Policies in the diagram.

## References
- https://rasa.com/docs/rasa/
- https://rasa.com/docs/rasa/arch-overview/
- https://www.python.org/downloads/release/python-3813/
