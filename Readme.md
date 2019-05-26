# MyGallery

    基于Bootstrap, jinja2 实现的个人摄影作品展示页面.
    A personal gallery page based on Bootstrap and jinja2.

## Structure

    .
    ├─assets                 
    │  ├─css                 
    │  │  └─themes           
    │  ├─fonts               
    │  ├─img                 
    │  │  └─prettyPhoto      
    │  ├─js
    │  └─img-info.json  --- 全部图片信息(尺寸, 分类)                
    ├─images            --- 待展示图片(原图)               
    │  └─compress       --- 压缩图片(预览图)           
    ├─src               --- 代码(渲染, 压缩图片, 统计信息)
    ├─_includes         --- 网页各部分模板                       
    └─index.html        --- 渲染出的页面                    

## Usage

1. 下载此仓库 <br>Download this repository
2. 将图片放入`/images`中 <br>Put photos into `/images`
3. 运行`/src/compress.py`压缩图片 <br>Compress photos by `/src/compress.py`
4. 运行`/src/img-stat.py`统计图片信息 <br>Get photos' info by `/src/img-stat.py`
5. 运行`/src/xr.py`渲染页面 <br>Render your page by `/src/xr.py`

## Note
- `/images` 文件夹里的图片没有被上传到github, 直接打开`index.html` *不会显示任何图片*.
- `/src/compress.py` 中使用 `tinify` 包需要 `key`, 默认存在 `/src/tinify-key` 文件中, 该文件没有被上传到github.

## TO-Do
- [ ] 分页 Pagination
- [ ] 提高加载速度 Speed up
- [ ] 图片上传后台系统 Photo upload system