class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for s in strs:
            en += "nova" + s + "neva"
        return en


    def decode(self, s: str) -> List[str]:
        de = []
        s = s.split("neva")
        for string in s:
            if string != "":
                string = string.replace("nova", "")
                de.append(string)
        return de
