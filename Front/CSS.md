在Antd的组件中，`style`属性可以用来设置一些常见的CSS样式属性，例如：

- `width`：设置元素的宽度。
- `height`：设置元素的高度。
- `margin`：设置元素的外边距。
- `padding`：设置元素的内边距。
- `backgroundColor`：设置元素的背景颜色。
- `color`：设置元素的文本颜色。
- `fontFamily`：设置元素的字体。
- `fontSize`：设置元素的字体大小。
- `fontWeight`：设置元素的字体粗细。
- `display`：设置元素的显示方式（如：`block`、`inline`、`flex`等）。
- `position`：设置元素的定位方式（如：`relative`、`absolute`等）。
- `top`、`right`、`bottom`、`left`：设置元素的定位偏移量。

这只是一些常见的CSS样式属性示例，实际上，你可以使用任何有效的CSS样式属性来设置`style`属性。

除了直接在`style`属性中设置CSS样式属性，你还可以传递一个对象来设置样式。例如：

```js
const styleObject = {
  width: '100px',
  height: '50px',
  backgroundColor: 'blue',
  color: 'white',
};

return <div style={styleObject}>Hello, Antd!</div>;
```

在上面的例子中，我们将一个包含CSS样式属性的对象传递给`style`属性，以设置`div`元素的样式。

# 属性

## display

### flex

`display: flex` 是 CSS 中的一个属性，用于指定一个元素的布局方式为弹性布局（flex布局）。

当你将一个元素的 `display` 属性设置为 `flex` 时，它会成为一个容器元素，其中的子元素会按照一定的规则进行布局。flex布局提供了强大的灵活性，可以轻松实现水平居中、垂直居中、等分空间等常见布局需求。

以下是一些 `display: flex` 的特点和用法：

- 弹性容器（Flex Container）：将一个元素的 `display` 属性设置为 `flex` 后，该元素就成为了一个弹性容器。它的子元素会成为弹性项目（Flex Item），并按照一定的规则进行布局。

- 主轴（Main Axis）和交叉轴（Cross Axis）：弹性容器具有主轴和交叉轴的概念。默认情况下，主轴是水平方向，交叉轴是垂直方向。你可以使用 `flex-direction` 属性来改变主轴的方向。

- 弹性项目（Flex Item）：弹性容器中的子元素称为弹性项目。你可以使用 `flex` 属性来控制弹性项目的伸缩性、占据空间的比例以及对齐方式等。

- 主轴对齐（Main Axis Alignment）：你可以使用 `justify-content` 属性来控制弹性项目在主轴上的对齐方式，例如居中对齐、靠左对齐、靠右对齐等。

- 交叉轴对齐（Cross Axis Alignment）：你可以使用 `align-items` 属性来控制弹性项目在交叉轴上的对齐方式，例如居中对齐、靠上对齐、靠下对齐等。

通过使用 `display: flex`，你可以轻松创建灵活的布局，并对其中的弹性项目进行对齐和排列。

#### flex-direction

设置主轴的方向，决定子元素的排列方式。可选值包括

- `row`：水平方向，从左到右排列（默认值）。
- `row-reverse`：水平方向，从右到左排列。
- `column`：垂直方向，从上到下排列。
- `column-reverse`：垂直方向，从下到上排列。

#### flex-wrap

设置是否允许子元素换行。可选值包括

- `nowrap`：不换行（默认值）。
- `wrap`：换行，按照主轴方向自动换行。
- `wrap-reverse`：换行，按照主轴方向自动换行，并反转换行顺序。

#### justify-content

设置子元素在主轴上的对齐方式。可选值包括：

- `flex-start`：靠左对齐（默认值）。
- `flex-end`：靠右对齐。
- `center`：居中对齐。
- `space-between`：两端对齐，子元素之间的间隔相等。
- `space-around`：子元素两侧的间隔相等。

#### align-items

设置子元素在交叉轴上的对齐方式。可选值包括：

- `flex-start`：顶部对齐。
- `flex-end`：底部对齐。
- `center`：居中对齐。
- `baseline`：基线对齐。
- `stretch`：拉伸以填充容器的高度（默认值）。
- `space-between`：弹性项目在主轴上平均分布，首个项目在起始位置，最后一个项目在结束位置，中间的项目之间间隔相等。
- `space-around`：弹性项目在主轴上平均分布，项目之间的间隔相等，包括首个项目和最后一个项目两侧的间隔是其他项目间隔的一半。
- `space-evenly`：弹性项目在主轴上平均分布，项目之间的间隔相等，包括首个项目和最后一个项目两侧的间隔也相等。

#### align-content

设置多行子元素在交叉轴上的对齐方式。可选值包括：

- `flex-start`：顶部对齐。
- `flex-end`：底部对齐。
- `center`：居中对齐。
- `space-between`：两端对齐，行之间的间隔相等。
- `space-around`：行两侧的间隔相等。
