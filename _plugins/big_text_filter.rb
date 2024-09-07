module Jekyll
  module BigTextFilter
    def big_text(input)
      # %%で囲まれた文字列を探し、<span class="big-text">タグで囲む
      input.gsub(/%%([^%]+)%%/) do
        "<span class='big-text'>#{$1}</span>"
      end
    end
  end
end

Liquid::Template.register_filter(Jekyll::BigTextFilter)
