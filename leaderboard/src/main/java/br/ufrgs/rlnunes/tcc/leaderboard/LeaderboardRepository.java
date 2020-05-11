package br.ufrgs.rlnunes.tcc.leaderboard;

import java.util.Optional;

import org.springframework.data.repository.CrudRepository;

public interface LeaderboardRepository extends CrudRepository<Leaderboard, Long> {
    Optional<Leaderboard> findById(Long id);
}