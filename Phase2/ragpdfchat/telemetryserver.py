# import phoenix as px
# from phoenix.otel import register
# from openinference.instrumentation.langchain import LangChainInstrumentor
# import os

# # Create a permanent folder in your user directory
# phoenix_dir = os.path.join(os.path.expanduser("~"), ".phoenix")
# if not os.path.exists(phoenix_dir):
#     os.makedirs(phoenix_dir)

# # Force Phoenix to use this directory instead of Temp
# os.environ["PHOENIX_WORKING_DIR"] = phoenix_dir


# # 1. Launch Phoenix (local UI defaults to http://localhost:6006)
# # Check if a session is already active before launching
# if px.active_session() is None:
#     session = px.launch_app()
# else:
#     session = px.active_session()
#     print(f"Phoenix already running at: {session.url}")


# # 2. Register and instrument LangChain
# tracer_provider = register()
# LangChainInstrumentor().instrument(tracer_provider=tracer_provider)

import os
import sys
import phoenix as px
from phoenix.otel import register
from openinference.instrumentation.langchain import LangChainInstrumentor

# --- CONFIGURATION ---
# 1. Use a local project folder for data to avoid Windows Temp locks
os.environ["PHOENIX_WORKING_DIR"] = os.path.join(os.getcwd(), ".phoenix_data")

# 2. Cleanup any existing sessions on the same port
try:
    active = px.active_session()
    if active:
        print("Closing existing Phoenix session...")
        active.stop()
except Exception:
    pass

# --- INITIALIZATION ---
print("Launching Phoenix...")
session = px.launch_app()

# Instrument LangChain
tracer_provider = register()
LangChainInstrumentor().instrument(tracer_provider=tracer_provider)

print(f"✅ Phoenix is live at: {session.url}")
