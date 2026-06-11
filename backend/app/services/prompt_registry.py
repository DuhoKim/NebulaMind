import os
import yaml
from pathlib import Path
import logging
import signal

logger = logging.getLogger(__name__)

class PromptRegistry:
    _instance = None
    _templates = {}
    _loaded = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, root_dir: str = None):
        if self._loaded:
            if root_dir is not None:
                self.root_dir = Path(root_dir)
            return
        if root_dir is None:
            # Resolve relative to the backend directory
            root_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "app/config/prompts/jury")
        self.root_dir = Path(root_dir)
        self.reload()
        self._setup_signal_handler()
        self._loaded = True

    def reload(self):
        """Loads or reloads YAML files from self.root_dir."""
        logger.info(f"Loading/reloading prompt templates from {self.root_dir}")
        new_templates = {}
        if self.root_dir.exists():
            for f in self.root_dir.glob("*.yaml"):
                template_name = f.stem
                try:
                    with open(f, "r", encoding="utf-8") as stream:
                        content = yaml.safe_load(stream)
                        if content:
                            new_templates[template_name] = content
                except Exception as e:
                    logger.error(f"Failed to load prompt template {f}: {e}")
        else:
            logger.warning(f"Prompt registry directory does not exist: {self.root_dir}")
        self._templates = new_templates
        logger.info(f"Loaded templates: {list(self._templates.keys())}")

    def _setup_signal_handler(self):
        """Register SIGHUP handler to reload templates dynamically."""
        try:
            if hasattr(signal, "SIGHUP"):
                def handle_sighup(signum, frame):
                    logger.info("Received SIGHUP signal. Reloading prompt registry...")
                    self.reload()

                signal.signal(signal.SIGHUP, handle_sighup)
                logger.info("Registered SIGHUP handler for prompt registry reloading.")
        except Exception as e:
            logger.warning(f"Failed to set up SIGHUP handler: {e}")

    def render(self, template_name: str, variables: dict, policy: str = "strict_v1") -> str:
        """Renders a template with variables using python's standard formatting."""
        if template_name not in self._templates:
            raise KeyError(f"Template '{template_name}' not found in registry.")

        data = self._templates[template_name]

        # Check if the YAML has top-level keys matching policies (like strict_v1, permissive_v1)
        if policy in data:
            policy_data = data[policy]
            if isinstance(policy_data, dict):
                template_str = policy_data.get("system_template") or policy_data.get("template") or ""
            else:
                template_str = str(policy_data)
        elif "system_template" in data:
            template_str = data["system_template"]
        elif "template" in data:
            template_str = data["template"]
        elif isinstance(data, dict):
            template_str = data.get("system_template") or data.get("template") or ""
        else:
            template_str = str(data)

        if not template_str:
            raise ValueError(f"No renderable template found for '{template_name}' under policy '{policy}'")

        # Perform Python standard string formatting
        try:
            return template_str.format(**variables)
        except KeyError as e:
            logger.error(f"Missing variable {e} for template {template_name} (policy: {policy})")
            raise
