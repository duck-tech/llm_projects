# Embedding Learning

這是一個學習如何透過langchain, 開發一個文件問答系統

## Project 目標

![alt text](./images/image-1.png)

## 實作

### Langchain loader

![alt text](./images/image-2.png)
![alt text](./images/image-3.png)

### The Entire Embedding Flow

![alt text](./images/image-4.png)
![alt text](./images/image-5.png)

### text_splitter

```python
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0,
)
```

![alt text](./images/image-6.png)

### embedding

![alt text](./images/image-7.png)

## chromaDB

- 每次執行都會重新創建db到chromaDB
![alt text](./images/image-8.png)
- 問題發生
![alt text](./images/image-9.png)

### Retrivel QA

![alt text](./images/image-10.png)

- Retriever: langchain 方便有一個接口, 對應不同DB
![alt text](./images/image-11.png)

- chain_type=stuff
![alt text](./images/image-12.png)

