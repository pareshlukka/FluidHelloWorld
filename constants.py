# constants.py

# --- Model & API Settings ---
MODEL = "gpt-4o-mini"   # LLM model to use
TEMP = 0.2              # Temperature (randomness)
TOKENS = 1024           # Max tokens for LLM responses

# --- Browser Settings ---
STEP_TIMEOUT = 12       # Max seconds for each step
VIEWPORT = (1900, 1080) # Chrome window size (width, height)
MAX_WAIT_READY = 8      # Wait max seconds for page ready

# --- Visual Comparison Settings ---
DIFF_THRESHOLD = 0.10   # % threshold for screenshot diff to detect visual changes
IMG_SIZE = (800, 450)   # Screenshot resize dimensions for faster LLM processing

# --- Network Capture Settings ---
NETWORK_BUFFER_SIZE = 10000000  # 10MB Chrome DevTools Protocol buffer size

# --- Form Inputs Settings ---
SEL_INPUTS_FIRST = [
    "input:not([type=hidden]):not([disabled])",
    "textarea:not([disabled])",
    "select:not([disabled])",
    "button:not([disabled])",
    "a[href]",
    "[role=button]:not([aria-disabled='true'])",
    "div[onclick]",
    "div[class*='click']",
    "*[tabindex='0']",
    "[role]:not([role='button']):not([aria-disabled='true'])",
    "div.interactive",
    "div[data-action]",
    "div.btn",
    "div[class*='button']",
    "[class*='clickable']",
    "[class*='selectable']",
    "[aria-haspopup='true']"
]

TEXT_TYPES = {
    "", "text", "email", "password", "search", "tel", "url", "number"
}

