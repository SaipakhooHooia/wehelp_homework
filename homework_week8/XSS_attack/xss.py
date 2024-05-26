from flask import Flask, request, render_template_string

app = Flask(__name__)

comments = []

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Comment Section</title>
    </head>
    <body>
        <h1>Article</h1>
        <p>This is an interesting article.</p>
        
        <h2>Comments</h2>
        <form method="post" action="/submit_comment">
            <textarea name="comment" placeholder="Leave a comment"></textarea>
            <button type="submit">Submit</button>
        </form>
        
        <div id="comments">
            {% for comment in comments %}
                <p>{{ comment|safe }}</p> <!-- 使用 safe 过滤器禁用 HTML 转义 -->
            {% endfor %}
        </div>
    </body>
    </html>
    ''', comments=comments)

@app.route('/submit_comment', methods=['POST'])
def submit_comment():
    comment = request.form['comment']
    comments.append(comment)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
