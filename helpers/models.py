from pydantic import BaseModel, HttpUrl, EmailStr, Field
from typing import Optional, List, Dict
from datetime import datetime


class Medias(BaseModel):
    url : Optional[str] =Field(... , description="Post media url")
    mediaType: Optional[str] =Field(... , description="Post media type")
    thumbnail_url: Optional[str] =Field(... , description="Post video thumbnail url")
    
    
class PostModel(BaseModel):
    id: str = Field(... , description= "Post ID in social media platform")
    url: str = Field(... , description= "Post url")
    description: str = Field(... , description= "Post text description")
    medias: Medias
    likes_count: str = Field(... , description= "likes count")
    comments_count: str = Field(... , description= "comments count")
    insights_count: str = Field(... , description= "views/engagemnt/reach count")
    bookmarked_counts: str = Field(... , description= "saved count")
    share_count: str = Field(... , description= "share count")
    quote_count: str = Field(... , description= "quoted retweets counts")
    repost_count: str = Field(... , description= "reposts/retweets counts")
    created_at: str = Field(... , description= "post creation datetime GMT")
    created_ts: str = Field(... , description= "post creation timestamp GMT")
    author_id: str = Field(... , description= "author id")
    author_url: str = Field(... , description= "author profile url")
    source: str = Field(... , description= "content source")
    source_type: str = Field(... , description= "source type")
    hashtags: str = Field(... , description= "post hashtags")
    mentioned_users: str = Field(... , description= "mentioned users in post")
    language: str = Field(... , description= "detected language of post")
    translated_description: str = Field(... , description= "english-translated post description text")
    sentiment: str = Field(... , description= "post sentiment")
    ner: str = Field(... , description= "ner post result")

    
    
class UserModel(BaseModel):
    id: str = Field(... , description= "User ID in social media platform")
    username: str = Field(... , description= "User ID in social media platform")
    name: str = Field(... , description= "User ID in social media platform")
    url: str = Field(... , description= "User ID in social media platform")
    profile_image_url: str = Field(... , description= "User ID in social media platform")
    cover_image_url: str = Field(... , description= "User ID in social media platform")
    created_at: str = Field(... , description= "User ID in social media platform")
    created_ts: str = Field(... , description= "User ID in social media platform")
    description: str = Field(... , description= "User ID in social media platform")
    location: str = Field(... , description= "User ID in social media platform")
    description: str = Field(... , description= "User ID in social media platform")
    urls: str = Field(... , description= "User ID in social media platform")
    hashtags: str = Field(... , description= "User ID in social media platform")
    tags: str = Field(... , description= "User ID in social media platform")
    verified: str = Field(... , description= "User ID in social media platform")
    verified_type: str = Field(... , description= "User ID in social media platform")
    type: str = Field(... , description= "User ID in social media platform")
    pinned_post_ids: str = Field(... , description= "User ID in social media platform")
    mentioned_users: str = Field(... , description= "User ID in social media platform")
    language: str = Field(... , description= "User ID in social media platform")
    average_posts_per_day: str = Field(... , description= "User ID in social media platform")
    likes_count: str = Field(... , description= "User ID in social media platform")
    followers_count: str = Field(... , description= "User ID in social media platform")
    friends_count: str = Field(... , description= "User ID in social media platform")
    views_count: str = Field(... , description= "User ID in social media platform")
    posts_count: str = Field(... , description= "User ID in social media platform")
    listed_count: str = Field(... , description= "User ID in social media platform")
    medias_count: str = Field(... , description= "User ID in social media platform")
    mentions_count: str = Field(... , description= "User ID in social media platform")
    sentiment: str = Field(... , description= "User ID in social media platform")
    
    
    
    