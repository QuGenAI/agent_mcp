class FileSystem:
    """File system operations"""
 
    def get_files(self,path: str) -> list:
        """Get all files in a directory"""
        import os
        return os.listdir(path)

    # @mcp.tool()
    def get_file_size(self,path: str) -> int:
        """Get the size of a file"""
        import os
        return os.path.getsize(path)

    # @mcp.tool()
    def get_file_extension(self,path: str) -> str:
        """Get the extension of a file"""
        import os
        return os.path.splitext(path)[1]

    # @mcp.tool()
    def merge_files(self,file1: str, file2: str) -> str:
        """Merge two files"""
        import os
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            return f1.read() + f2.read()
        
    # @mcp.tool()
    def copy_file(self,src: str, dest: str) -> str:
        """Copy a file"""
        import shutil
        shutil.copy(src, dest)
        return f"Copied {src} to {dest}"

    # @mcp.tool()
    # def move_file(src: str, dest: str) -> str:
    #     """Move a file"""
    #     import shutil
    #     shutil.move(src, dest)
    #     return f"Moved {src} to {dest}"


