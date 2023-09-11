# Table

`columns` 是一个配置表格列的属性，它接收一个数组，每个元素表示一个列的配置。每个列的配置可以包含以下字段：

1. `title`：列的标题，可以是字符串或 React 组件。
2. `dataIndex`：列数据在数据项中对应的字段名，用于渲染对应的数据。
3. `key`：列的唯一标识，通常是数据项中的唯一字段。
4. `render`：自定义列的渲染函数，可以根据需要对列的内容进行自定义渲染。
5. `width`：列的宽度，可以是一个字符串或数字类型的值。
6. `align`：列的对齐方式，可以是 `'left'`、`'center'` 或 `'right'`。
7. `ellipsis`：是否自动省略超长内容，默认为 `false`。
8. `fixed`：是否固定列，可以是 `'left'`、`'right'` 或 `true`（固定在左侧）。
9. 其他可用的属性还包括 `sorter`、`filters`、`onFilter`、`filterMultiple`、`filterDropdown` 等，用于实现排序、筛选等功能。

以下是一个示例，展示了如何使用 `columns` 配置表格列：

```jsx
const columns = [
  {
    title: '姓名',
    dataIndex: 'name',
    key: 'name',
  },
  {
    title: '年龄',
    dataIndex: 'age',
    key: 'age',
  },
  {
    title: '地址',
    dataIndex: 'address',
    key: 'address',
  },
];

<Table columns={columns} dataSource={data} />
```

在上述示例中，我们定义了一个包含三列的 `columns` 数组，每个列都有 `title`、`dataIndex` 和 `key` 字段。

你可以根据需要在每个列的配置中添加或修改字段，以满足你的表格需求。


