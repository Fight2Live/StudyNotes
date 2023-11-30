# 声明

## 变量

### 区别

```go
matchRange := new(*[]models.ModelDataInfosPoint)
matchRange := make([]models.ModelDataInfosPoint, 0)
var matchRange *[]models.ModelDataInfosPoint
```

这三种声明方式有以下区别：

1. `matchRange := new(*[]models.ModelDataInfosPoint)`：这种方式使用了 `new` 关键字来创建一个指向 `[]models.ModelDataInfosPoint` 类型的指针。`matchRange` 的类型是 `*[]models.ModelDataInfosPoint`，即指向切片的指针。在这种方式中，`matchRange` 还没有被初始化，因此其值为 `nil`。

2. `matchRange := make([]models.ModelDataInfosPoint, 0)`：这种方式使用了 `make` 关键字来创建一个长度为 0 的切片。`matchRange` 的类型是 `[]models.ModelDataInfosPoint`，即切片类型。在这种方式中，`matchRange` 被初始化为空切片。

3. `var matchRange *[]models.ModelDataInfosPoint`：这种方式声明了一个指向 `[]models.ModelDataInfosPoint` 类型的指针变量 `matchRange`，但是没有初始化它。在这种方式中，`matchRange` 的值为 `nil`。

因此，这三种声明方式的主要区别在于它们创建的变量类型和初始化方式不同。根据具体的使用场景和需求，选择适合的声明方式可以提高代码的可读性和效率。

# 指针

## 值打印

在 Go 语言中，可以通过在指针变量前加上 `*` 符号来访问指针指向的值。例如，假设有一个指向 `int` 类型变量的指针变量 `p`，可以使用以下代码打印指针指向的值：

```go
var p *int
// ...
fmt.Println(*p)
```

在上述代码中，`*p` 表示访问指针 `p` 指向的值。如果 `p` 指向的是一个 `int` 类型的变量，那么 `*p` 就是这个变量的值。

类似地，如果有一个指向自定义类型的指针变量 `q`，可以使用以下代码打印指针指向的值：

```go
type MyStruct struct {
    // ...
}

var q *MyStruct
// ...
fmt.Println(*q)
```

在上述代码中，`*q` 表示访问指针 `q` 指向的值，即一个 `MyStruct` 类型的变量。

需要注意的是，如果指针变量为 `nil`，即指向空地址，那么访问指针指向的值会导致运行时错误。因此，在访问指针指向的值之前，需要确保指针变量指向了一个有效的地址。

## 切片和指针

`[]*FeatureRule` 和 `*[]FeatureRule` 是两种不同的类型。

`[]*FeatureRule` 表示一个指向 `FeatureRule` 指针的切片类型，可以存储多个 `FeatureRule` 指针。例如：

```go
var featureRules []*FeatureRule
```

上述代码中，`featureRules` 是一个指向 `FeatureRule` 指针的切片类型，可以存储多个 `FeatureRule` 指针。

`*[]FeatureRule` 表示一个指向 `FeatureRule` 切片的指针类型，可以指向一个 `FeatureRule` 切片变量。例如：

```go
var featureRules []FeatureRule
var featureRulesPtr *[]FeatureRule
featureRulesPtr = &featureRules
```

上述代码中，`featureRules` 是一个 `FeatureRule` 切片类型的变量，`featureRulesPtr` 是一个指向 `FeatureRule` 切片的指针类型的变量，指向了 `featureRules` 变量。

在使用时，`[]*FeatureRule` 和 `*[]FeatureRule` 有以下不同：

- `[]*FeatureRule` 可以使用 `append` 函数向切片中添加新元素，而 `*[]FeatureRule` 不支持直接使用 `append` 函数，需要先对指向的切片进行初始化。
- `[]*FeatureRule` 可以直接使用索引访问切片中的元素，例如 `featureRules[0]`，而 `*[]FeatureRule` 需要先通过指针访问切片，例如 `(*featureRulesPtr)[0]`。
- `[]*FeatureRule` 可以使用 `range` 关键字遍历切片中的元素，例如 `for _, rule := range featureRules`，而 `*[]FeatureRule` 需要先通过指针访问切片，例如 `for _, rule := range *featureRulesPtr`。

需要根据具体的需求选择合适的类型。如果需要在函数之间传递切片类型的参数，并且需要在函数内部向切片中添加新元素，可以使用 `[]*FeatureRule` 类型。如果需要在函数之间传递指向切片的指针类型的参数，并且不需要在函数内部向切片中添加新元素，可以使用 `*[]FeatureRule` 类型。

# 坑

## for range遍历时的地址不变问题

现有结构体：

```go
type Customer struct {
    id   int
    name string
    age  int

}
```

对其进行遍历

```go
func main() {

    var customerData []Customer
    customerData = append(customerData, Customer{id: 1, name: "a", age: 10})
    customerData = append(customerData, Customer{id: 2, name: "b", age: 20})
    customerData = append(customerData, Customer{id: 3, name: "c", age: 30})


    for _, item := range customerData {
        fmt.Println("id: ", item.id)
        fmt.Printf("item地址：%p\n", &item)
        fmt.Println("item值：", item)
        fmt.Println("------------")
    }

}
```

        是因为在开始for range遍历时，会创建一个item对象，因为**只在开始时创建，所以地址是固定的**，当遍历时，只是将遍历到的数据传递进item里。所以会出现如果打印item的值，那么是变化的，而如果打印地址，则会发现地址不变的情况。

        要想在循环里获取到每一个item对象的地址，比如转成`map[int]*Customer`的形式，那需要在在循环中把item赋给一个新的对象，然后用新的对象来操作，如：

```go
func main() {

    var customerData []Customer
    customerData = append(customerData, Customer{id: 1, name: "a", age: 10})
    customerData = append(customerData, Customer{id: 2, name: "b", age: 20})
    customerData = append(customerData, Customer{id: 3, name: "c", age: 30})

    var customerDataMap map[int]*Customer

    for _, item := range customerData {
        newItem := item
        customerDataMap[item.id] = &newItem
        fmt.Printf("新item地址：%p\n", &newItem )
        fmt.Println("新item值：", newItem )
        fmt.Println("================")
    }

}
```
