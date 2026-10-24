from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated AI generation function
def generate_seo_metadata(content):
    # sends a prompt to an LLM
    word_count = len(content.split())
    return {
        "title_tag": f"Optimized Title for {word_count} words",
        "meta_description": f"An AI-generated summary of the provided text, optimized for search engine click-through rates. Contains {word_count} words of context.",
        "focus_keywords": ["AI Web Development", "SEO Automation", "Python"]
    }

@app.route('/api/generate-seo', methods=['POST'])
def handle_seo_generation():
    data = request.get_json()
    if not data or 'content' not in data:
        return jsonify({"error": "Missing content payload"}), 400
    
    seo_data = generate_seo_metadata(data['content'])
    return jsonify({"status": "success", "data": seo_data}), 200

if __name__ == '__main__':
    app.run(port=8080, debug=True)
