# MathMatrixMovies

MathMatrixMovies is an AI-powered platform that generates engaging, personalized math explainer videos from simple text prompts. By leveraging Google's Gemini Pro 1.5 and Manim, the tool creates high-quality animations tailored to any age group or skill level, revolutionizing math education.

Check out the live demo at [https://math.auto.movie](https://math.auto.movie)

Watch an example video on YouTube: [5+3=8 Explained for 3-Year-Olds](https://www.youtube.com/watch?v=-4-M8YwAlhU)

Read the blog post about how it works [here](https://medium.com/@aditya-advani/deep-dive-creating-accurate-math-videos-using-llms-02db22ba1d2d)


## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/MathMatrixMovies.git
cd MathMatrixMovies
```

2. Set up a virtual environment and install the required packages. We have used Python 3.10.12 & Python 3.11.9 successfully:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Set up the following environment variables:
```
export AZURE_SUBSCRIPTION_KEY=""
export AZURE_SERVICE_REGION=""
export GOOGLE_API_KEY=""
export MANIM_BIN="/home/azureuser/m3-hack/MathMatrixMovies/venv/bin/manim"
export GROQ_API_KEY=""
```

4. Set up Azure Text-to-Speech (TTS) by following the instructions from the [Manim Community Voiceover Plugin documentation](https://voiceover.manim.community/en/latest/installation.html).

5. Install Manim and its prerequisites by following the instructions from the [Manim Community documentation](https://docs.manim.community/en/stable/installation.html).

6. You will also need to install the [Groq API](https://wow.groq.com/) by following the instructions from the [Groq API documentation](https://wow.groq.com/).

7. Finally you will need a Gemini API key by following the instructions from the [Google AI Studio Dev](https://ai.google.dev/).


## Usage

To run the frontend (what you want when testing the repo):
```
streamlit run ui.py
```

To host the request form:
```
streamlit run request_ui.py
```

To generate a test video, run the following command:
```
manim -ql <manim_script.py>
```

Replace `<manim_script.py>` with the name of your Manim script file. Using the frontend is the easiest way to get started.


## Contributing

We welcome contributions to improve MathMatrixMovies. Please feel free to submit pull requests or open issues on our GitHub repository.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Acknowledgments

- [Manim Community](https://manim.community/) for the amazing math animation library
- [Manim Voiceover Plugin](https://voiceover.manim.community/) for the amazing math animation library's voiceover plugin
- [Google Gemini Pro 1.5](https://gemini.google.com/) for the powerful language model
- [Meta Llama3](https://llama3.meta.com/) for the open-source language model


## Contact

If you have any questions or would like to contribute to the project, feel free to reach out to us individually:

- Aditya Advani - on twitter [@aditya_advani](https://twitter.com/aditya_advani)
- Baladhurgesh B - on twitter [@baladhurgesh97](https://twitter.com/baladhurgesh97)
- Lily X Su - on twitter [@excelsiorpred](https://twitter.com/excelsiorpred)
- Justin B Strong - on twitter [@gptjustin](https://twitter.com/gptjustin)

Happy math video generating!

