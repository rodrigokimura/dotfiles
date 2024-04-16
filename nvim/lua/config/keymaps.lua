-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua

vim.api.nvim_create_user_command("LazyTerm", function(opts)
  print(string.format("LazyTerm #%s", opts.count))
  LazyVim.terminal(nil, { cwd = LazyVim.root(), env = { LAZYTERM_COUNT = opts.count } })
end, { count = 1 })

for i = 1, 5, 1 do
  vim.keymap.set(
    { "n", "t" },
    string.format("<A-%s>", i),
    string.format("<cmd> %sLazyTerm <cr>", i),
    { desc = "Open terminal" }
  )
end

-- Debugger
local dap = require("dap")
vim.keymap.set("n", "<leader>d<space>", dap.continue, { desc = "Continue" })
vim.keymap.set("n", "<leader>dm", require("dap-python").test_method, { desc = "Debug test method" })
vim.keymap.set("n", "<leader>dc", require("dap-python").test_class, { desc = "Debug test class" })
vim.keymap.set("n", "<leader>dt", function()
  require("neotest").run.run({ strategy = "dap" })
end, { desc = "Debug nearest test" })
vim.keymap.set("n", "<leader>dT", require("neotest").summary.toggle, { desc = "Toggle test summary" })

-- Resize terminal
vim.keymap.set("t", "<A-k>", "<cmd>resize +2<cr>", { desc = "Increase window height" })
vim.keymap.set("t", "<A-j>", "<cmd>resize -2<cr>", { desc = "Decrease window height" })

-- Resize window
vim.keymap.set("n", "<SA-h>", "<cmd>vertical resize +2<cr>", { desc = "Increase window width" })
vim.keymap.set("n", "<SA-l>", "<cmd>vertical resize -2<cr>", { desc = "Decrease window width" })
vim.keymap.set("n", "<SA-j>", "<cmd>resize +2<cr>", { desc = "Increase window height" })
vim.keymap.set("n", "<SA-k>", "<cmd>resize -2<cr>", { desc = "Decrease window height" })

vim.keymap.set({ "n", "i", "v" }, "<C-w>", function()
  require("mini.bufremove").delete(0, false)
end, { desc = "Delete Buffer" })

vim.keymap.set("n", "-", require("oil").open, { desc = "Open parent directory" })
