package br.ufrgs.rlnunes.tcc.leaderboard;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;

@Entity
@Data
@Builder
@AllArgsConstructor
public class Leaderboard {

  @Id
  @GeneratedValue(strategy = GenerationType.AUTO)
  private Long id;

  private LeaderboardStatus status;

  protected Leaderboard() {
  }

  public Leaderboard(LeaderboardStatus status) {
    this.status = status;
  }
}