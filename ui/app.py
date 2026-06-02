"""
Member B — Streamlit UI
Query input, tool trace panel, cited answer display
"""

import sys
import os
import streamlit as st

sys.path.append(os.path.join(os.path.dirname(__file__), "../agent"))
from agent import run_agent

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="News Research Assistant",
    page_icon="📰",
    layout="wide"
)

st.title("📰 News Research Assistant")
st.caption("Agentic · RAG · MCP · Multi-source citations")

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")
    show_trace = st.toggle("Show tool trace", value=True)
    st.divider()
    st.markdown("**Tech Stack**")
    st.markdown("- RAG: ChromaDB + embeddings")
    st.markdown("- Agent: Claude Sonnet")
    st.markdown("- MCP: 8 custom tools")
    st.markdown("- Eval: 4-layer harness")

# ── Query Input ───────────────────────────────────────────────────────────────
query = st.text_input(
    "Enter your research question",
    placeholder="e.g. What are the latest AI developments from OpenAI?",
)

col1, col2 = st.columns([1, 5])
with col1:
    run_btn = st.button("🔍 Research", type="primary", use_container_width=True)

# ── Run Agent ─────────────────────────────────────────────────────────────────
if run_btn and query:
    with st.spinner("Agent is researching..."):
        result = run_agent(query, verbose=False)

    # ── Answer ────────────────────────────────────────────────────────────────
    st.divider()
    st.subheader("📋 Answer")
    st.markdown(result["answer"])

    # ── Sources ───────────────────────────────────────────────────────────────
    chunks = result.get("chunks_used", [])
    if chunks:
        st.divider()
        st.subheader("📚 Sources Used")
        seen_urls = set()
        for chunk in chunks:
            url = chunk.get("url", "")
            if url in seen_urls:
                continue
            seen_urls.add(url)
            with st.expander(f"🔗 {chunk.get('source', 'Unknown')} — {chunk.get('date', '')[:10]}"):
                st.markdown(f"**{chunk.get('title', '')}**")
                st.markdown(f"[Read full article]({url})")
                st.caption(chunk.get("text", "")[:300] + "...")

    # ── Tool Trace ────────────────────────────────────────────────────────────
    if show_trace and result.get("tool_trace"):
        st.divider()
        st.subheader("🔧 Agent Tool Trace")
        for i, step in enumerate(result["tool_trace"], 1):
            with st.expander(f"Step {i}: `{step['tool']}`"):
                st.json(step["inputs"])
                st.caption(f"Result preview: {step['result_preview'][:200]}")

elif run_btn and not query:
    st.warning("Please enter a research question.")
