# Discord News Bot & Web Crawler
> This is the bot and web crawler for GEN2002X Sudox Project

> Currently the web crawler will only collect data from [https://www.scamalert.sg/]
## Folder Structure

- `DiscordNewsBot`
    - `discordBot`
        - `ScamGuardBot.py` (Change database info inside to your own database)
    - `scamAlert`
        - `scamAlert`
            - `_init_.py`
            - `items.py`
            - `middlewares.py`
            - `pipelines.py` (Change database info inside to your own database)
            - `settings.py`
        - extra files
    - `README.md`

    ## Prerequisites

    Before running this project, make sure you have the following installed:

    - Python 3.8+
    - Scrapy (install using `pip install scrapy`)
    - discord.py (install using `pip install discord.py`)

    You can check your Python version by running `python --version` in your terminal/command prompt.

    Once you have installed the prerequisites, you can proceed with running the project.

    ## Run
    To run this project, follow these steps:

    1. Open a terminal or command prompt.

    2. Navigate to the directory where the project is located. 

    3. Run the web crawler using Scrapy by executing the following command:  
    `scrapy crawl scamAlert`

    4. If you want to schedule the web crawler to run automatically, you can add it to the system's task scheduler. For example, on Windows, you can use the Task Scheduler to create a task that runs the command `scrapy crawl scamAlert` every 30 minutes.

    5. After running the web crawler, you can run the ScamGuardBot.py script. Make sure to provide the necessary database information inside the script. You can run the script using the following command:  
    `python DiscordNewsBot/discordBot/ScamGuardBot.py`

    6. To ensure that the process continues running even after you disconnect from the server, you can use tools like nohup or screen. For example, you can run the following command to start the script in the background and prevent it from being terminated when you disconnect:  
    `nohup python DiscordNewsBot/discordBot/ScamGuardBot.py`  
    This will run the script in the background and keep it running even after you disconnect.

    Make sure to replace the paths and file names with the correct ones based on your project structure.




