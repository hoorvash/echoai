import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure OpenAI API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_poem(text, input_lang="Persian", output_lang="Persian", genre="Pop"):
    """
    Generate a song lyric from input text using ChatGPT
    """
    prompt = f"""Turn the following text into a fully structured, professional song lyric. If it's a poem, refine it for better rhythm, rhyme, and musicality. If it's prose, transform it into a song with verses, chorus, and bridge. The song should be written in the style of the most highly recognized songwriter in {output_lang}, ensuring it follows their lyrical structure, depth, and emotional impact. Ensure the lyrics fit a melody naturally and are suitable for professional musical composition in {genre} style.

Output should be in this exact format with no extra explanation:

(Verse 1)
[First verse]

(Chorus)
[Chorus]

(Verse 2)
[Second verse]

(Bridge)
[Bridge if needed]

(Chorus - Repeat)

Input language: {input_lang}
Output language: {output_lang}
Genre: {genre}

Here is my text:
{text}"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an elite songwriter with deep knowledge of each language's most celebrated musical artists. You excel at capturing their signature style while creating original, emotionally resonant lyrics."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,  # For creative variations
            max_tokens=1000   # For longer songs
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating lyrics: {str(e)}"

def main():
    st.title("EchoAI Lyric Generator")
    st.write("Transform your thoughts into professional song lyrics using AI")

    # Input text
    user_text = st.text_area("Enter your text:", height=150)

    # Create three columns for selections
    col1, col2, col3 = st.columns(3)
    
    with col1:
        input_lang = st.selectbox(
            "Input language:",
            ["Persian", "English", "Arabic", "French", "Spanish"],
            index=0
        )
    
    with col2:
        output_lang = st.selectbox(
            "Output language:",
            ["Persian", "English", "Arabic", "French", "Spanish"],
            index=0
        )
    
    with col3:
        genre = st.selectbox(
            "Music Genre:",
            ["Pop", "Rock", "Folk", "Hip Hop", "R&B", "Classical", "Jazz"],
            index=0
        )

    # Generate button with styling
    if st.button("Generate Lyrics", type="primary"):
        if user_text:
            with st.spinner("Creating your lyrics..."):
                lyrics = generate_poem(user_text, input_lang, output_lang, genre)
                st.markdown("### Your Song Lyrics:")
                # Display lyrics in a nice format
                st.markdown(f"""
                ```
                {lyrics}
                ```
                """)
        else:
            st.warning("Please enter some text to generate lyrics.")

    # Add some helpful tips
    with st.expander("Tips for better results"):
        st.markdown("""
        - Provide emotionally rich text with vivid imagery
        - Include specific themes or metaphors you want to preserve
        - Longer input text will generate more detailed songs
        - The output will be styled after renowned songwriters in your chosen language
        - Different genres will affect the lyrical structure and style
        """)

if __name__ == "__main__":
    main() 