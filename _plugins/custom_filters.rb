module Jekyll
  module CustomFilters
    # カスタムフィルター: 指定した文字数で抜粋を生成
    def custom_excerpt(input, length = 50)
      input = input.to_s # 入力を文字列として扱う
      excerpt = input.split[0, length].join(" ")
      return excerpt + "..." if input.split.size > length
      excerpt
    end
  end
end

Liquid::Template.register_filter(Jekyll::CustomFilters)
