class AddSubtitleToInfographic < ActiveRecord::Migration
  def change
    add_column :infographics, :subtitle, :string
  end
end
