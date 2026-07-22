class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = "##SPLIT##".join(strs)
        new_str = f"###{len(strs)}###{new_str}"
        return new_str

    def decode(self, s: str) -> List[str]:
        length = int(s.split("###")[1])
        if length == 0:
            return []
        
        return s.replace(f"###{length}###", "").split("##SPLIT##")