"""Function handling module for SkibidiLang."""

from typing import List, Dict, Any
from dataclasses import dataclass

@dataclass
class Function:
    """Represents a function in SkibidiLang."""
    params: List[str]
    body: List[str]
    parent_scope: Dict[str, Any]

    def __init__(self, params: List[str], body: List[str], parent_scope: Dict[str, Any]):
        """
        Initialize a function.
        
        Args:
            params: List of parameter names.
            body: List of code lines in the function body.
            parent_scope: Dictionary containing the scope where the function was defined.
        """
        self.params = params
        self.body = body
        self.parent_scope = dict(parent_scope)  # Create a copy of the scope
