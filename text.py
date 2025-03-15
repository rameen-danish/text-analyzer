import streamlit as st

# Page title with styling
st.set_page_config(page_title="Text Analyzer", page_icon="📝", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🔍 Text Analyzer</h1>", unsafe_allow_html=True)
st.write("Analyze your text efficiently with word count, character count, case conversion, and more!")

# User Input
text = st.text_area("📜 Enter a paragraph:", height=150)

if text:
    st.divider()  # Adds a horizontal line

    # Word & Character Count
    word_count = len(text.split())
    char_count = len(text)

    # Vowel Count
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)

    # Search & Replace
    with st.expander("🔍 Find and Replace"):
        search_word = st.text_input("Enter a word to search:")
        replace_word = st.text_input("Enter a word to replace it with:")
        modified_text = text.replace(search_word, replace_word) if search_word else text

    # Case Conversion
    upper_text = text.upper()
    lower_text = text.lower()

    # Operators
    contains_python = "Python" in text
    avg_word_length = char_count / word_count if word_count > 0 else 0

    # Display Results in Columns
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="📖 Total Words", value=word_count)
        st.metric(label="🔡 Total Characters", value=char_count)
        st.metric(label="🔠 Vowel Count", value=vowel_count)

    with col2:
        st.metric(label="🔢 Avg. Word Length", value=f"{avg_word_length:.2f}")
        st.metric(label="🐍 Contains 'Python'?", value="✅ Yes" if contains_python else "❌ No")

    st.divider()

    # Modified Text Output
    st.subheader("📝 Modified Paragraph")
    st.info(modified_text)

    # Case Conversion Display
    with st.expander("🔤 Case Conversion"):
        st.success(f"🔼 **Uppercase:**\n\n{upper_text}")
        st.warning(f"🔽 **Lowercase:**\n\n{lower_text}")

else:
    st.warning("⚠️ Please enter a paragraph to analyze.")

# Footer
st.markdown("<br><hr><center>Made with ❤️ using Streamlit by Rameen Rashid</center>", unsafe_allow_html=True)
