require 'test_helper'

class InfographicsControllerTest < ActionController::TestCase
  setup do
    @infographic = infographics(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:infographics)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create infographic" do
    assert_difference('Infographic.count') do
      post :create, infographic: { chart_type: @infographic.chart_type, source: @infographic.source, title: @infographic.title }
    end

    assert_redirected_to infographic_path(assigns(:infographic))
  end

  test "should show infographic" do
    get :show, id: @infographic
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @infographic
    assert_response :success
  end

  test "should update infographic" do
    put :update, id: @infographic, infographic: { chart_type: @infographic.chart_type, source: @infographic.source, title: @infographic.title }
    assert_redirected_to infographic_path(assigns(:infographic))
  end

  test "should destroy infographic" do
    assert_difference('Infographic.count', -1) do
      delete :destroy, id: @infographic
    end

    assert_redirected_to infographics_path
  end
end
