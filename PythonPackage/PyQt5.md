



## 大小策略

当使用Qt编程时，`QSizePolicy`是一个用于控制小部件（widget）大小策略的类。它定义了小部件在布局中如何调整大小的行为。

`QSizePolicy`类具有以下几个重要的属性：

- `QSizePolicy.Policy`: 这是一个枚举类型，用于定义水平和垂直方向上的大小策略。常用的策略包括：
  - `QSizePolicy.Fixed`：固定大小，小部件将保持固定的宽度和高度。
  - `QSizePolicy.Minimum`：最小尺寸，小部件将尽可能小，以适应其内容。
  - `QSizePolicy.Maximum`：最大尺寸，小部件将尽可能大，以填充可用空间。
  - `QSizePolicy.Preferred`：首选尺寸，小部件将尽可能接近其推荐大小。
  - `QSizePolicy.MinimumExpanding`：最小扩展尺寸，小部件将尽可能小，但允许扩展以填充可用空间。
  - `QSizePolicy.MaximumExpanding`：最大扩展尺寸，小部件将尽可能大，但允许收缩以适应可用空间。
- `QSizePolicy.ControlType`：这是一个枚举类型，用于定义小部件的控制类型。常用的类型包括：
  - `QSizePolicy.DefaultType`：默认类型，小部件的大小策略由其父级布局决定。
  - `QSizePolicy.ButtonBox`：按钮框类型，小部件通常用于按钮组合框。
  - `QSizePolicy.CheckBox`：复选框类型，小部件通常用于复选框。
  - `QSizePolicy.ComboBox`：组合框类型，小部件通常用于下拉列表框。
  - `QSizePolicy.Frame`：框架类型，小部件通常用于框架或边框。
  - `QSizePolicy.Label`：标签类型，小部件通常用于标签。
  - `QSizePolicy.Line`：线类型，小部件通常用于分隔线。
  - `QSizePolicy.PushButton`：推按钮类型，小部件通常用于按钮。
  - `QSizePolicy.RadioButton`：单选按钮类型，小部件通常用于单选按钮。
  - `QSizePolicy.Slider`：滑块类型，小部件通常用于滑块。
  - `QSizePolicy.SpinBox`：旋转框类型，小部件通常用于旋转框。
  - `QSizePolicy.TabWidget`：选项卡小部件类型，小部件通常用于选项卡小部件。
  - `QSizePolicy.ToolButton`：工具按钮类型，小部件通常用于工具按钮。

通过使用`QSizePolicy`，你可以根据需要设置小部件的大小策略，以便在布局中获得期望的大小行为。这样可以实现自定义布局和界面的设计。
