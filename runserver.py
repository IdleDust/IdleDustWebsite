from myapp import app
import os

port = int(os.environ.get("PORT", 8888));
host = "127.0.0.1";
app.run(host=host, port=port, debug=True);

