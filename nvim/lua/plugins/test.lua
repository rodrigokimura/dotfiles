return {
  {
    "nvim-neotest/neotest",
    dependencies = {
      "nvim-lua/plenary.nvim",
      "nvim-treesitter/nvim-treesitter",
      "antoinemadec/FixCursorHold.nvim",
      "haydenmeade/neotest-jest",
      "nvim-neotest/neotest-python",
    },
    config = function()
      local opts = {
        adapters = {
          require("neotest-jest")({
            jestCommand = "npm test --",
            -- jestConfigFile = "custom.jest.config.ts",
            env = { CI = true },
            cwd = function(path)
              return vim.fn.getcwd()
            end,
          }),
          require("neotest-python")({
            runner = "pytest",
            env = {
              PYTHONPATH = ".",
            },
            is_test_file = function(filepath)
              return string.sub(filepath, -3) == ".py"
                and (string.sub(filepath, -8) == "tests.py" or not not string.find(filepath, "test_", 0, true))
            end,
          }),
        },
        summary = {
          mappings = {
            run = "r",
            debug = "d",
            stop = "s",
            output = "o",
          },
        },
      }
      require("neotest").setup(opts)
    end,
  },
}
