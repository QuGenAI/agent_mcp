from mcp.server.fastmcp import FastMCP
import math

# mcp = FastMCP("Hello World")

class Calculator:
    # @mcp.tool()
    def add(self,a: int, b: int) -> int:
        """Add given both numbers"""
        return int(a + b)

    # @mcp.tool()
    def subtract(self,a: int, b: int) -> int:
        """Subtract given both numbers"""
        return int(a - b)

    # @mcp.tool()
    def multiply(self,a: int, b: int) -> int:
        """Multiply given both numbers"""
        return int(a * b)

    # @mcp.tool() 
    def divide(self,a: int, b: int) -> float:
        """Divide given both numbers"""
        return float(a / b)

    # @mcp.tool()
    def power(self,a: int, b: int) -> int:
        """Divide given both numbers"""
        return int(a ** b)

    # @mcp.tool()
    def sqrt(self,a: int) -> float:
        """Squre root of given number"""
        return float(a ** 0.5)

    # @mcp.tool()
    def factorial(self,a: int) -> int:
        """Get the factorial of given number"""
        return int(math.factorial(a))


    # @mcp.tool()
    def remainder(self,a: int, b: int) -> int:
        """Get the remainder of two numbers divison"""
        return int(a % b)