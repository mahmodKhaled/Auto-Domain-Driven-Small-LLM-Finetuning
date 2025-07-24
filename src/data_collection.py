import wikipedia
from typing import List, Dict

class DataCollector:
    def __init__(
        self
    ) -> None:
        pass

    def search_wikipedia(
        self,
        topic: str,
        max_results: int
    ) -> List[str]:
        search_results = wikipedia.search(topic, results=max_results)
        return search_results

    def get_page_content(
        self,
        page_title: str
    ) -> Dict[str, str]:
        try:
            wikipedia.set_lang("en")
            
            page = wikipedia.page(page_title)
            return {
                'title': page.title,
                'content': page.content,
                'url': page.url,
                'summary': page.summary,
            }
        except Exception as e:
            return None
