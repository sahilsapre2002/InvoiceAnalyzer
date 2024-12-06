# InvoiceAnalyzer
Developed a Streamlit-based application integrated with Google's Gemini API to perform OCR on images, enabling analysis and generative insights from textual data (e.g., invoices). The project involved user input handling, image preprocessing, and API-driven content generation.

In the context of **OCR (Optical Character Recognition)**, this code sets up a **Streamlit web application** that leverages **Google’s Gemini API** to analyze textual and image data. Here's the OCR-specific breakdown:

1. **Image Upload and Preprocessing**:
   - Users can upload an image (e.g., invoice or document) using Streamlit's `file_uploader`.
   - The uploaded image is displayed on the app using **Pillow (PIL)**.

2. **Image Data Preparation**:
   - The `input_image_setup` function prepares the uploaded image for processing by converting it into raw bytes and capturing its MIME type. This format is necessary for the Gemini API to analyze the image.

3. **OCR via Google Gemini API**:
   - The `get_gemini_respond` function sends the user-provided text, the image, and a prompt to the **Gemini-Pro-Vision model**, which combines OCR capabilities with generative AI to understand and analyze the content in the image.

4. **Interactive Output**:
   - While the current implementation lacks a fully connected workflow, the app is intended to generate and display the extracted and interpreted text from the image (e.g., invoice details) upon clicking the **"Tell me about the Invoice"** button.

This workflow demonstrates integrating OCR with an advanced AI model to not just extract text but also generate context-aware responses, like summarizing or interpreting an invoice.
