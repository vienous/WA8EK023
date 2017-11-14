# Interview questions
## 基本概念

 1. 操作系统中 heap 和 stack 的区别 
    * heap是堆，stack是栈。
    * stack的空间由操作系统自动分配和释放，heap的空间是手动申请和释放的，heap常用new关键字来分配。
    * stack空间有限，heap的空间是很大的自由区。
    在Java中，若只是声明一个对象，则先在栈内存中为其分配地址空间，若再new一下，实例化它，则在堆内存中为其分配地址。
    
    **栈内存**：在函数中定义的一些基本类型的变量和对象的引用变量都在函数的栈内存中分配。 栈内存主要存放的是基本类型类型的数据 如、( int, short, long, byte, float, double, boolean, char) 和对象句柄。并没有有String基本类型、在栈内存的数据的大小及生存周期是必须确定的、其优点是寄存速度快、、栈数据可以共享、缺点是数据固定、不够灵活。
    
    栈的共享：
    ```java
    String a = "abc";
    String b = "abc";
    System.out.println(a==b);//true
    ```
    
    **堆内存**：
    堆内存用来存放所有new 创建的对象和 数组的数据、
    
    ```java
    String a = new String ("abc");
    String b = "abc";
    System.out.println(a==b);  //false
    String a = new String ("abc");
    String b = new String ("abc");
    System.out.println(a==b);  //false
    ```
 2. 什么是基于注解的切面实现
 3. 什么是 对象/关系 映射集成模块
 4. 什么是 Java 的反射机制
 5. 什么是 ACID
 6. BS与CS的联系与区别
 7. Cookie 和 Session的区别
 8. fail-fast 与 fail-safe 机制有什么区别
 9. get 和 post请求的区别
 10. Interface 与 abstract 类的区别
 11. IOC的优点是什么
 12. IO 和 NIO的区别，NIO优点
 13. Java 8 / Java 7 为我们提供了什么新功能
 14. 什么是竞态条件？ 举个例子说明。
 15. JRE、JDK、JVM 及 JIT 之间有什么不同
 16. 什么是控制反转（Inversion of Control）与依赖注入（Dependency Injection）
 17. MVC的各个部分都有那些技术来实现?如何实现?
 18. RPC 通信和 RMI 区别 
 19. 什么是 Web Service（Web服务）
 20. JSWDL开发包的介绍。JAXP、JAXM的解释。SOAP、UDDI,WSDL解释。 
 21. WEB容器主要有哪些功能? 并请列出一些常见的WEB容器名字。
 22. 一个".java"源文件中是否可以包含多个类（不是内部类）？有什么限制
 23. 简单说说你了解的类加载器。是否实现过类加载器
 24. 解释一下什么叫AOP（面向切面编程）
 25. 请简述 Servlet 的生命周期及其相关的方法
 26. 请简述一下 Ajax 的原理及实现步骤
 27. 简单描述Struts的主要功能
 28. 什么是 N 层架构
 29. 什么是CORBA？用途是什么
 30. 什么是Java虚拟机？为什么Java被称作是“平台无关的编程语言”
 31. 什么是正则表达式？用途是什么？哪个包使用正则表达式来实现模式匹配
 32. 什么是懒加载（Lazy Loading）
 33. 什么是尾递归，为什么需要尾递归
 

