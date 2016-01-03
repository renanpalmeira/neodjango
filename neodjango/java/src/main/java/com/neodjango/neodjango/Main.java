package com.neodjango.neodjango;

import org.neo4j.graphdb.GraphDatabaseService;
import org.neo4j.graphdb.factory.GraphDatabaseFactory;

public class Main {
	private static final String GRAPH_PATH = "";

	public static void main(String[] args) {
		GraphDatabaseFactory graphDbFactory = new GraphDatabaseFactory();
		GraphDatabaseService graphDb = graphDbFactory.newEmbeddedDatabase(GRAPH_PATH);
		
		System.out.println("Connecting to neo4j.....");
	}
}