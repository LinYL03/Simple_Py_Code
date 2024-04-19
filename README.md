[TOC]



# Py代码练习

一些简单的py代码

# 一些常见的问题

## # 无法提交

当出现如下的报错信息时：

```
Git: fatal: unable to access 'https://github.com/LinYL03/Simple_Py_Code.git/': Failed to connect to github.com port 443 after 21054 ms: Couldn't connect to server
```

好厚米的解释是：这个错误提示说明了 Git 在尝试连接 GitHub 时出现了问题。具体来说，它无法通过 HTTPS 访问 GitHub，因为无法连接到 github.com 的 443 端口，连接超时了。这可能是由于网络问题、防火墙设置、代理配置或 GitHub 服务器问题等原因引起的。要解决这个问题，你可以尝试以下几种方法：

1. **检查网络连接**：确保你的网络连接正常，尝试使用浏览器访问 GitHub 网站来确认是否能够连接。
2. **检查防火墙和代理设置**：如果你使用了防火墙或代理服务器，请确保其设置不会阻止 Git 连接到 GitHub。你可能需要配置防火墙或代理以允许 Git 的访问。
3. **尝试使用 SSH 协议**：如果你的网络环境允许，可以尝试使用 SSH 协议而不是 HTTPS 协议来进行 Git 操作。这样可以避免某些网络问题，但需要设置 SSH 密钥。
4. **尝试使用 VPN**：有时候使用 VPN 可以解决网络连接问题，你可以尝试连接到一个可靠的 VPN 服务并再次尝试 Git 操作。
5. **等待一段时间**：有时候 GitHub 服务器可能出现临时问题，稍等一段时间再次尝试可能会解决问题。

如果以上方法都无法解决问题，建议你查看 Git 的错误日志，其中可能会提供更多有关连接失败的详细信息，以便进一步诊断问题。

解决之后发现是网络问题。

