def get_transcript(video_id):
    transcripts = {
        "aircAruvnKk": """
        Neural networks are systems of neurons connected in layers.
        They learn patterns using weights and activation functions.
        """,

        "wjZofJX0v4M": """
        Transformers use self attention to process sequences in parallel.
        They solve long range dependency problems better than RNNs.
""",

        "fHF22Wxuyw4": """
        Deep learning is a subset of machine learning.
        It uses multiple layers to learn data representations.
        """,

        "C6YtPJxNULA": """
        Overfitting occurs when a model memorizes training data.
        It fails to generalize to new unseen data.
        """
    }

    return transcripts.get(video_id, "")
