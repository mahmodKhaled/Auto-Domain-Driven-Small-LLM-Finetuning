import os
from src.data_collection import DataCollector
from src.utils import load_config, create_colored_logger, save_str_to_txt

logger = create_colored_logger()

def finetune_pipeline(
    config: dict
) -> None:
    # Data Collection
    topic_name = config.get("topic_domain")
    num_articles = config.get("num_articles")
    logger.info(f"Starting Data Collection for topic: {topic_name}, num_articles: {num_articles}")

    collector = DataCollector()
    topic_titles = collector.search_wikipedia(topic_name, num_articles)
    logger.info(f"Found {len(topic_titles)} articles for {topic_name} topic")

    for title in topic_titles:
        page_content = collector.get_page_content(title)
        if page_content:
            file_path = os.path.join("data/raw", f'{topic_name}', f"{page_content['title']}.txt")
            save_str_to_txt(page_content["content"], file_path)
            logger.info(f"Successfully retrieved content for {title} Article")
        else:
            logger.warning(f"Failed to retrieve content for {title} Article")

if __name__ == "__main__":
    config_path = "config.yaml"
    config = load_config(config_path)

    finetune_pipeline(config)
