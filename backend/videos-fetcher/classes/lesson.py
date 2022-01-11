class lesson:
    def __init__(self,title : str) -> None:
        self.title = title
        self.videos_list = None
        
    def set_videos_list(self, videos_list):
        self.videos_list = videos_list
        