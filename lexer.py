"""Lexer module for SkibidiLang."""

from dataclasses import dataclass
from typing import List

from constants import KEYWORDS
from exceptions import SkibidiSyntaxError

@dataclass
class Token:
    """Represents a token in the SkibidiLang."""
    type: str
    value: str

class SkibidiLexer:
    """Lexical analyzer for SkibidiLang."""
    
    def __init__(self):
        """Initialize the lexer."""
        self.tokens: List[Token] = []

    def tokenize(self, code: str) -> List[Token]:
        """
        Convert source code into a list of tokens.
        
        Args:
            code: The source code to tokenize.
            
        Returns:
            List of Token objects.
            
        Raises:
            SkibidiSyntaxError: If invalid syntax is encountered.
        """
        self.tokens = []
        
        # Remove comments first
        code = code.split('#')[0].strip()
        if not code:
            return []
            
        words = code.split()
        i = 0
        
        try:
            while i < len(words):
                word = words[i]
                
                # Check for two-word keywords
                if i < len(words) - 1:
                    two_words = f"{word} {words[i+1]}"
                    if two_words in KEYWORDS:
                        self.tokens.append(Token(KEYWORDS[two_words], two_words))
                        i += 2
                        continue

                # Check for strings (in quotes)
                if word.startswith('"') and word.endswith('"'):
                    self.tokens.append(Token('STRING', word[1:-1]))
                # Single word keywords
                elif word in KEYWORDS:
                    self.tokens.append(Token(KEYWORDS[word], word))
                # Numbers
                elif word.isdigit() or (word.startswith('-') and word[1:].isdigit()):
                    self.tokens.append(Token('NUMBER', word))
                # Variables/Identifiers
                elif word.isalnum():
                    self.tokens.append(Token('IDENTIFIER', word))
                # Operators and special characters
                elif word in '+-*/=:':
                    self.tokens.append(Token('OPERATOR', word))
                else:
                    raise SkibidiSyntaxError(f"Invalid token: {word}")
                
                i += 1
            
            return self.tokens
            
        except SkibidiSyntaxError as e:
            raise
        except Exception as e:
            raise SkibidiSyntaxError(f"Error during tokenization: {str(e)}")
