# Unity2D开发指北 实现角色跳跃

由于刚体本身受重力影响，我们只要给角色一个向上的初始速度，就能实现平滑的跳跃

若玩家按下跳跃键且角色处于地面上，则给予一个向上的速度

```c#
// Jump()代码每帧调用
private void Jump()
{
    if (!(Input.GetButton("Jump") && IsGround())) return;// 若未按下键就不判断是否在地面了，减少运算量
    _playerBody.velocity = new Vector2(_playerBody.velocity.x, jumpHeight);

}

private bool IsGround()
{
    return _playerColliderBox.IsTouchingLayers(LayerMask.GetMask("Ground"));
}
```

注意：

- `GetButton()`检测按键是否在按下状态，`GetButtonDown()`和`GetButtonUp()`则是检测按键从弹起到按下（以及反之）的状态变化

  所以，前者可以实现按住空格连跳，后两者则不行