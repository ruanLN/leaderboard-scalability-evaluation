package br.ufrgs.rlnunes.tcc.leaderboard;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Leaderboard {

  @Id
  @GeneratedValue(strategy=GenerationType.AUTO)
  private Long id;
  
  private LeaderboardStatus status;

  protected Leaderboard() {}

  public Leaderboard(LeaderboardStatus status) {
      this.status = status;
  }

  public Long getId() {
    return id;
  }

  public LeaderboardStatus getStatus() {
      return status;
  }

  public Leaderboard withId(Long id) {
      this.id = id;
      return this;
  }

  public Leaderboard withStatus(LeaderboardStatus status) {
    this.status = status;
    return this;
}
}