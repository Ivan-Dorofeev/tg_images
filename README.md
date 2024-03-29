# tg_images
Get images from NASA, SpaceX and send to telegram channel.

![image](https://user-images.githubusercontent.com/58893102/218962612-810d9fec-53bd-4349-b555-d9f93785f75f.png)


# Information
All images downloads to folder "/image".

# Install
First of all, install packages from **_requirements.txt_**:

```python pip -m install -r requirements.txt```

Then you need to create file ".env" and add two variables:
>TG_BOT_TOKEN=[....your telegram token...]
>
>SKY_iIMAGES_CHANNEL_CHAT_ID=[....chat_id....]

Script take values of this variables and use:

>tg_token = os.environ['TG_BOT_TOKEN']
> 
>chat_id = os.environ['SKY_iIMAGES_CHANNEL_CHAT_ID']



# Run
Download images from SpaceX (by id launch):

```python fetch_spacex_images.py 67```
> 67 - id launch (example)


Download images from SpaceX (last launch):

```python fetch_spacex_images.py```


Download 5 EPIC images from NASA:

```python fetch_nasa_epic_images.py```


Download 5 APOD images from NASA:

```python fetch_nasa_apod_images.py```


Automatic send images in the entered time interval from folder '/image':

```python bot.py 4```
> 4 - time interval (hours)

# Errors
If no last launch image, you will see:

> "Извините, нет фото последнего запуска на сайте"


