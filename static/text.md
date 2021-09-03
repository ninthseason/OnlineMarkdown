# jQuery 食用指北

> 万能公式：`$(selector).action()`

## 选择器

**选择器选择出的是jQuery包装后的element(暂称之jelement)，而不是element**

jelement可以通过索引获得element，如`jelement[0]`

element可以通过`$(element)`获取其jelement

jQuery大部分操作只能对jelement进行

### 标签选择器

```js
$('标签名')
```

### 类选择器

```js
$('.类名')
```

### id选择器

```js
$('#id')
```

**jQuery选择器语法与css选择器相同**

## 事件

### 文档加载完毕

```js
// jQuery
$(document).ready(function () {
    alert(1)
})
```

```js
// jQuery简写
$(function () {
    alert(1)
})
```

### 单击 onclick

```js
// 原生js
document.getElementsByTagName('h1')[0].onclick = function () {
    alert(1)
}
```

```js
// jQuery
$('h1').click(function () {
    alert(1);
})
```

###  鼠标移动 mousemove

```js
$('#MoveDomain').mousemove()
```

鼠标移动是**频繁触发**事件

## 属性

### 文本内容 text

```js
$('#ShowPos').text() // 获取文本内容
```

```js
$('#ShowPos').text('value') // 修改文本内容
```

### 样式表 css

**注意：css的读取会读取优先级最高的样式，写入会直接写在标签的style里面**

```js
$('#MoveDomain').css('border') // 获取border属性的值
```

```js
$('#MoveDomain').css('border', 'red solid') // 修改border属性的值
```

注意：css方法必须传入属性键参数

一次设置多个样式：

```js
$('#MoveDomain').css({'border': 'red solid', 'background': 'red', ...})
```

---

隐藏/显示元素 快捷方法

```js
$('#MoveDomain').hide()
```

```js
$('#MoveDomain').show()
```

**本质是修改了元素display样式**

---

显示隐藏切换 toggle

```js
$('#MoveDomain').toggle()
```

若元素隐藏则显示，反之反之

### 高度 height

```js
$('#MoveDomain').height() // 获取
$('#MoveDomain').height(100) // 修改
```

### 宽度 width

```js
$('#MoveDomain').width() // 获取
$('#MoveDomain').width(100) // 修改
```