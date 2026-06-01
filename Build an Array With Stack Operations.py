class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        operations = []
        target_idx = 0
        current_stream_num = 1
        
        while target_idx < len(target):
            operations.append("Push")
            
            if current_stream_num == target[target_idx]:
                target_idx += 1
            else:
                operations.append("Pop")
                
            current_stream_num += 1
            
        return operations