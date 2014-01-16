class CreateInfographics < ActiveRecord::Migration
  def change
    create_table :infographics do |t|
      t.string :title
      t.string :source
      t.string :chart_type

      t.timestamps
    end
  end
end
